from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from precipitation import Precipitation
from temperature import Temperature
from solar import Solar
from water_level import Water_level
import csv
import methods
import numpy

class MainWindow:
    def __init__(self):
        # create data storage
        self.precipitation = {}
        self.precipitation_key = []
        self.water_level = {}
        self.water_level_key = []
        self.max_temperature = {}
        self.max_temperature_key = []
        self.min_temperature = {}
        self.min_temperature_key = []
        self.solar_exposure = {}
        self.solar_exposure_key = []
        # create weight for ANN
        self.w1 = numpy.random.randn()
        self.w2 = numpy.random.randn()
        self.w3 = numpy.random.randn()
        self.w4 = numpy.random.randn()
        self.b = numpy.random.randn()
        # create a the widgets
        # create a windows object
        self.root = Tk()
        self.root.title("Flood Prediction System")
        self.root.geometry("1000x500")
        # create a header for the app
        self.Header = Label(self.root, text="Flood Prediction System", bg="black", fg="white", font=10)
        self.Header.pack(fill=X)
        # create a menu object inside a windows
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        # create a submenu inside a menu call fileMenu
        self.fileMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Import Precipitation", command=lambda: self.read_csv("precipitation"))
        self.fileMenu.add_command(label="Import Water Level", command=lambda: self.read_csv("water_level"))
        self.fileMenu.add_command(label="Import Max Temperature", command=lambda: self.read_csv("max_temperature"))
        self.fileMenu.add_command(label="Import Min Temperature", command=lambda: self.read_csv("min_temperature"))
        self.fileMenu.add_command(label="Import Solar Exposure", command=lambda: self.read_csv("solar_exposure"))
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Export Chart")
        self.fileMenu.add_command(label="Export Text File")
        # create a command in menu object call About
        self.menu.add_command(label="About")
        # create a combobox for draw scatterplot
        self.combo_1 = ttk.Combobox(self.root)
        self.combo_1['values'] = ('Select Data Set', 'Water Level', 'Precipitation', 'Max Temperature',
                                  'Min Temperature', 'Solar Exposure')
        self.combo_1.current(0)
        self.combo_1.place(x=120, y=60, anchor="center")
        self.combo_2 = ttk.Combobox(self.root)
        self.combo_2['values'] = ('Select Data Set', 'Water Level', 'Precipitation', 'Max Temperature',
                                  'Min Temperature', 'Solar Exposure')
        self.combo_2.current(0)
        self.combo_2.place(x=280, y=60, anchor="center")
        # create button for draw scatter plot
        self.scatter_button = Button(self.root, text="Scatter Plot", command= lambda: methods.draw_scatter_connect(
            self.combo_1, self.combo_2, self.precipitation, self.water_level, self.max_temperature, self.min_temperature,
            self.solar_exposure, self.precipitation_key, self.water_level_key, self.max_temperature_key,
            self.min_temperature_key, self.solar_exposure_key))
        self.scatter_button.place(x=410, y=60, anchor="center")
        # create a combobox for calculate corr
        self.combo_3 = ttk.Combobox(self.root)
        self.combo_3['values'] = ('Select Data Set', 'Water Level', 'Precipitation', 'Max Temperature',
                                  'Min Temperature', 'Solar Exposure')
        self.combo_3.current(0)
        self.combo_3.place(x=120, y=120, anchor="center")
        self.combo_4 = ttk.Combobox(self.root)
        self.combo_4['values'] = ('Select Data Set', 'Water Level', 'Precipitation', 'Max Temperature',
                                  'Min Temperature', 'Solar Exposure')
        self.combo_4.current(0)
        self.combo_4.place(x=280, y=120, anchor="center")
        # create button for calculate corr
        self.corr_button = Button(self.root, text="Correlation", command= lambda: self.get_corr(
            self.combo_3, self.combo_4, self.precipitation, self.water_level, self.max_temperature, self.min_temperature,
            self.solar_exposure, self.precipitation_key, self.water_level_key, self.max_temperature_key,
            self.min_temperature_key, self.solar_exposure_key))
        self.corr_button.place(x=410, y=120, anchor="center")
        self.text_output = Text(self.root, height=15, width=42)
        self.text_output.place(x=700, y=180, anchor="center")
        # Making prediction function interface
        #add a Max Temperature lable
        self.lmaxtemp = Label(self.root, text="Max Temperature (Celsius)")
        self.lmaxtemp.place(x=100, y=220, anchor="center")
        #add a text entry for Max Temperature
        self.emaxtemp = Entry(self.root)
        self.emaxtemp.place(x=100, y=240, anchor="center")
        #add a Min Temperature lable
        self.lmintemp = Label(self.root, text="Min Temperature (Celsius)")
        self.lmintemp.place(x=250, y=220, anchor="center")
        #add a text entry for Min Temperature
        self.emintemp = Entry(self.root)
        self.emintemp.place(x=250, y=240, anchor="center")
        #add a Rainfall lable
        self.lrainfall = Label(self.root, text="Rainfall (Millimeter)")
        self.lrainfall.place(x=100, y=280, anchor="center")
        #add a text entry for Rainfall
        self.erainfall = Entry(self.root)
        self.erainfall.place(x=100, y=300, anchor="center")
        #add a Solar lable
        self.lsolar = Label(self.root, text="Solar (MJ/m*m)")
        self.lsolar.place(x=250, y=280, anchor="center")
        #add a text entry for Solar
        self.esolar = Entry(self.root)
        self.esolar.place(x=250, y=300, anchor="center")
        # create button for Training ANN
        self.train_button = Button(self.root, text="Training ANN", command=lambda: self.training_ann(
            self.precipitation, self.water_level, self.max_temperature,
            self.min_temperature,
            self.solar_exposure, self.precipitation_key, self.water_level_key, self.max_temperature_key,
            self.min_temperature_key, self.solar_exposure_key, self.etrain.get()))
        self.train_button.place(x=400, y=240, anchor="center")
        # create button for Prediction
        self.Predict_button = Button(self.root, text="Predict", command=lambda: self.predict(
            self.emaxtemp.get(), self.emintemp.get(), self.erainfall.get(), self.esolar.get()))
        self.Predict_button.place(x=400, y=300, anchor="center")
        ##add a Training Times lable
        self.ltrain = Label(self.root, text="Training Times")
        self.ltrain.place(x=250, y=150, anchor="center")
        #add a text entry for Training Times
        self.etrain = Entry(self.root)
        self.etrain.place(x=250, y=180, anchor="center")
    def read_csv(self, file_type):
        if file_type == "precipitation":
            print("read precipitation")
            fileaddress = askopenfilename()
            precipitations = {}
            keys = []
            with open(fileaddress) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                count = 0
                for row in readCSV:
                    year = row[2]
                    month = row[3]
                    day = row[4]
                    amount = row[5]
                    location = row[1]
                    key = year+month+day
                    if count > 0:
                        precipitations[key] = Precipitation(year, month, day, amount, location)
                        keys.append(key)
                    count +=1
            self.precipitation.update(precipitations)
            self.precipitation_key = self.precipitation_key + keys
            print(len(keys))
        elif file_type == "water_level":
            print("read water_level")
            fileaddress = askopenfilename()
            water_level = {}
            keys = []
            with open(fileaddress) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    date = row[0]
                    date_list = date.split(" ")
                    year = date_list[2]
                    month = date_list[1]
                    month = methods.month_con(month)
                    month = str(month)
                    day = date_list[0]
                    water = row[3]
                    key = year + month + day
                    water_level[key] = Water_level(year, month,day, water)
                    keys.append(key)
            self.water_level.update(water_level)
            self.water_level_key = self.water_level_key + keys
            print(len(keys))
        elif file_type == "max_temperature":
            print("read max_temperature")
            fileaddress = askopenfilename()
            max_temperatures = {}
            keys = []
            with open(fileaddress) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                count = 0
                for row in readCSV:
                    year = row[2]
                    month = row[3]
                    day = row[4]
                    temp = row[5]
                    location = row[1]
                    key = year + month + day
                    if count > 0:
                        max_temperatures[key] = Temperature(year, month, day, temp, location)
                        keys.append(key)
                    count += 1
            self.max_temperature.update(max_temperatures)
            self.max_temperature_key = self.max_temperature_key + keys
            print(len(keys))
        elif file_type == "min_temperature":
            print("read min_temperature")
            fileaddress = askopenfilename()
            min_temperatures = {}
            keys = []
            with open(fileaddress) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                count = 0
                for row in readCSV:
                    year = row[2]
                    month = row[3]
                    day = row[4]
                    temp = row[5]
                    location = row[1]
                    key = year + month + day
                    if count > 0:
                        min_temperatures[key] = Temperature(year, month, day, temp, location)
                        keys.append(key)
                    count += 1
            self.min_temperature.update(min_temperatures)
            self.min_temperature_key = self.min_temperature_key + keys
            print(len(keys))
        elif file_type == "solar_exposure":
            print("read solar exposure")
            fileaddress = askopenfilename()
            solar_exposure = {}
            keys = []
            with open(fileaddress) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                count = 0
                for row in readCSV:
                    year = row[2]
                    month = row[3]
                    day = row[4]
                    solar = row[5]
                    location = row[1]
                    key = year + month + day
                    if count > 0:
                        solar_exposure[key] = Solar(year, month, day, solar, location)
                        keys.append(key)
                    count += 1
            self.solar_exposure.update(solar_exposure)
            self.solar_exposure_key = self.solar_exposure_key + keys
            print(len(keys))

    def get_corr(self, combo_1, combo_2, precipitation, water_level, max_temperature, min_temperature, solar_exposure,
                      precipitation_key, water_level_key, max_temperature_key, min_temperature_key, solar_exposure_key):
        corr = methods.calculate_cor_connect(combo_1, combo_2, precipitation, water_level, max_temperature, min_temperature, solar_exposure,
                      precipitation_key, water_level_key, max_temperature_key, min_temperature_key, solar_exposure_key)
        corr = str(corr)
        self.text_output.insert("insert", "The correlation is: "+str(corr)+ "\n")

    def training_ann(self, precipitation, water_level, max_temperature, min_temperature, solar_exposure,
                      precipitation_key, water_level_key, max_temperature_key, min_temperature_key, solar_exposure_key, training_time):
        train_set = methods.making_training_set(precipitation, water_level, max_temperature, min_temperature, solar_exposure,
                      precipitation_key, water_level_key, max_temperature_key, min_temperature_key, solar_exposure_key)
        new_train_set = methods.delete_data_rain_0(train_set)
        training_result = methods.training(new_train_set, int(training_time))
        self.w1 = training_result[0]
        print('w1 = ' + str(self.w1))
        self.w2 = training_result[1]
        print('w2 = ' + str(self.w2))
        self.w3 = training_result[2]
        print('w3 = ' + str(self.w3))
        self.w4 = training_result[3]
        print('w4 = ' + str(self.w4))
        self.b = training_result[4]
        print('b = ' + str(self.b))


    def predict(self, max_temp, min_temp, rainfall, solar):
        result = ((float(max_temp) * self.w1 + float(min_temp) *
                  self.w2 + float(rainfall) * self.w3 + float(solar) * self.w4 + self.b)/1000000)-1
        self.text_output.insert("insert", "The predict result: "+str(result) + "\n")
        return result


if __name__ == "__main__":
    window = MainWindow()
    mainloop()