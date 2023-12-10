import pandas as pd
import numpy as np

# constants
phi     = 52.239333      # latitude degrees
gravity = 9.8            # gravitational acceleration 
earth_av = 0.0041667     # angular velocity of earth in degrees/sec it is 0.2618 radian/sec
# read the data from csv files 

# when x axis is pointing down
x_down_one = pd.read_csv("Calibration_Data/x_down_one.csv", delimiter="\t")
x_down_two = pd.read_csv("Calibration_Data/x_down_two.csv", delimiter="\t")

# when x axis is pointing up
x_up_one = pd.read_csv("Calibration_Data/x_up_one.csv", delimiter="\t")
x_up_two = pd.read_csv("Calibration_Data/x_up_two.csv", delimiter="\t")

# when y axis is pointing down
y_down_one = pd.read_csv("Calibration_Data/y_down_one.csv", delimiter="\t")
y_down_two = pd.read_csv("Calibration_Data/y_down_two.csv", delimiter="\t")

# when y axis is pointing up
y_up_one = pd.read_csv("Calibration_Data/y_up_one.csv", delimiter="\t")
y_up_two = pd.read_csv("Calibration_Data/y_up_two.csv", delimiter="\t")

# when z axis is pointing down
z_down_one = pd.read_csv("Calibration_Data/z_down_one.csv", delimiter="\t")
z_down_two = pd.read_csv("Calibration_Data/z_down_two.csv", delimiter="\t")

# when z axis is point up
z_up_one = pd.read_csv("Calibration_Data/z_up_one.csv", delimiter="\t")
z_up_two = pd.read_csv("Calibration_Data/z_up_two.csv", delimiter="\t")


# acceleration bias and scale factor
avr_acc_x_up   = np.mean([x_up_one['Acc_X'].mean(), x_up_two['Acc_X'].mean()])
avr_acc_x_down = np.mean([x_down_one['Acc_X'].mean(), x_down_two['Acc_X'].mean()])

avr_acc_y_up   = np.mean([y_up_one['Acc_Y'].mean(), y_up_two['Acc_Y'].mean()])
avr_acc_y_down = np.mean([y_down_one['Acc_Y'].mean(), y_down_two['Acc_Y'].mean()])

avr_acc_z_up   = np.mean([z_up_one['Acc_Z'].mean(), z_up_two['Acc_Z'].mean()])
avr_acc_z_down = np.mean([z_down_one['Acc_Z'].mean(), z_down_two['Acc_Z'].mean()])

# accelerometer bias
bias_acc_x = (avr_acc_x_up + avr_acc_x_down)/2
bias_acc_y = (avr_acc_y_up + avr_acc_y_down)/2
bias_acc_z = (avr_acc_z_up + avr_acc_z_down)/2

# accelerometer scale factor
sf_acc_x = (avr_acc_x_up - avr_acc_x_down - 2*gravity)/ (2*gravity)
sf_acc_y = (avr_acc_y_up - avr_acc_y_down - 2*gravity)/ (2*gravity)
sf_acc_z = (avr_acc_z_up - avr_acc_z_down - 2*gravity)/ (2*gravity)

# angular velocity bias and scale factor
avr_omega_x_up   = np.mean([x_up_one['Gyr_X'].mean(), x_up_two['Gyr_X'].mean()])
avr_omega_x_down = np.mean([x_down_one['Gyr_X'].mean(), x_down_two['Gyr_X'].mean()])

avr_omega_y_up   = np.mean([y_up_one['Gyr_Y'].mean(), y_up_two['Gyr_Y'].mean()])
avr_omega_y_down = np.mean([y_down_one['Gyr_Y'].mean(), y_down_two['Gyr_Y'].mean()])

avr_omega_z_up   = np.mean([z_up_one['Gyr_Z'].mean(), z_up_two['Gyr_Z'].mean()])
avr_omega_z_down = np.mean([z_down_one['Gyr_Z'].mean(), z_down_two['Gyr_Z'].mean()])

# gyroscope bias
bias_gyro_x = (avr_omega_x_up + avr_omega_x_down)/2
bias_gyro_y = (avr_omega_y_up + avr_omega_y_down)/2
bias_gyro_z = (avr_omega_z_up + avr_omega_z_down)/2

# gyrcope scale factor 
sf_gyro_x = (avr_omega_x_up - avr_omega_x_down - 2* earth_av * np.sin(np.deg2rad(phi))) / (2 * earth_av * np.sin(np.deg2rad(phi)))
sf_gyro_y = (avr_omega_y_up - avr_omega_y_down - 2* earth_av * np.sin(np.deg2rad(phi))) / (2 * earth_av * np.sin(np.deg2rad(phi)))
sf_gyro_z = (avr_omega_z_up - avr_omega_z_down - 2* earth_av * np.sin(np.deg2rad(phi))) / (2 * earth_av * np.sin(np.deg2rad(phi)))

# convert everything to csv file
data = {
    "Axis" : ['X', 'Y', "Z"],
    "Avr Acc up" : [avr_acc_x_up, avr_acc_y_up, avr_acc_z_up],
    "Avr Acc down" : [avr_acc_x_down, avr_acc_y_down, avr_acc_z_down],
    "Avr Gyr up" : [avr_omega_x_up, avr_omega_y_up, avr_omega_z_up],
    "Avr Gyr down" : [avr_omega_x_down, avr_omega_y_down, avr_omega_z_down],
    "Acc bias" : [bias_acc_x, bias_acc_y, bias_acc_z],
    "Acc SF" : [sf_acc_x, sf_acc_y, sf_acc_z],
    "Gyro bias" : [bias_gyro_x, bias_gyro_y, bias_gyro_z],
    "Gyro SF" : [sf_gyro_x, sf_gyro_y, sf_gyro_z]
}

data_frame = pd.DataFrame(data)
data_frame.to_csv('output.csv',index=False)