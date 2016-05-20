import csv
import numpy as np
import matplotlib.pyplot as plt

fname_non = "non_country.csv"
fname_pop = "population.csv"
fname_murder = "murder.csv"


class Data:

  data = []
  file_dict = {}
  var_dict = {}

  def __init__(self, fname):
    "Reads csv files and returns their contents in a dictionary"
    file = open(fname,encoding='utf-8')
    self.file_dict = csv.reader(file)

  def select_data(self, non_countries, lower_bound, upper_bound, latest_year=2016):
    """Removes country codes, that have no murder rate.
      countries: Dictionary
                 Complete data for all countries
      non_countries: Dictionary
                     Dictionary of all non-countries, which need to be removed from the country list
      lower_bound, upper_bound : int
             Describe the timespan of historic data to be taken from the dictionary
      latest_year: int
              The latest year included in  the data"""
    lower_bound = latest_year - lower_bound
    upper_bound = latest_year - upper_bound
    r=0
    for row in self.file_dict:
      r += 1
      if r > 5:
        if not (row[1] in non_countries):
          data = self.remove_empty( list(row[-lower_bound:-upper_bound]) )
          average = sum(data)/ float(len(data))
          self.var_dict[row[1]] = average

  def make_list(self, dictionary, no_country):
    """Returns a list corresponding to a dictionary"""
    for row in dictionary:
      if not (row in no_country):
        self.data.append(dictionary[row])

  def remove_empty(self, unconform_list):
    """Removes zero values and parenthesis, and converts to float in a list"""
    for row in range(len(unconform_list)):
      if unconform_list[row] == '':
        unconform_list[row] = 0
      unconform_list[row] = float(unconform_list[row])
    return unconform_list

  def make_array(self, non_array):
    """Create a numpy array from a list"""
    return np.array(non_array[1:])


no_country = Data(fname_non)
popul = Data(fname_pop)
murder = Data(fname_murder)

for row in no_country.file_dict:
  no_country.var_dict = row

popul.select_data(no_country.var_dict, 2000, 2014)
murder.select_data(no_country.var_dict, 2000, 2014)

popul.make_list(popul.var_dict, no_country.file_dict)
murder.make_list(murder.var_dict, no_country.file_dict)

popul.data = popul.make_array(popul.data)
murder.data = murder.make_array(murder.data)

#The data is fine now. So lets abandon the class and keep the values for future use

norm_pop = 1e-6 * popul.data

yrs = 1e5/murder.data

log_yrs = np.log10(yrs)

lmin,lmax = np.min(log_yrs),np.max(log_yrs)
bins = np.linspace(lmin,lmax,21)
bins = 10**bins

plt.xkcd()
plt.hist(yrs,bins,weights=norm_pop)
plt.gca().set_xscale('log')
plt.xlabel('Murder rate (per 100000 per yr)')
plt.ylabel('Population')
plt.show()

