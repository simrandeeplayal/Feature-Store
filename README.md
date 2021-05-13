# Feature-Store

The Config.ini file helps to declare file paths so the user do not need to change anything in init file. Once, the package files are installed in the local system the user only needs to change the geotiff file paths in config files.

The main file of the python package is “__init__.py”. Python treats the folder as a module if it contains the “__init__.py” file. Additionally, since this is the first file loaded in a package, you can use it to run code that you want to run any time the module is loaded or to define the submodules to be exported. The init file will have the following methods:

a)	Reading the Raster files
The package is able to read raster data from Geotiff files. Here Rasterio library is used to read files. It outputs the Geotiff file in an array that consists of feature values. These feature values can be extracted using x,y values. 

b)	Displaying Map
The package also have a method to visualise the raster map. Here, since the soil raster data is of Australia. The map of Australia is shown. 

c)	Feature Extract using featureextract method
Particular soil feature value can be extracted from the Geotiff file using featureextract() method which is defined in the package. This method will take two input values; x and y. These two values are Latitude and longitude. Once the method is called with the parameters the method will return a soil value. Using the affine transformation the latitude and longitude values will transform into new x and y values which are used to traverse through the array and find a particular value. 

d)	Merge Data
Another functionality of the package is to merge the feature values with any file. For example, if you have your own raw data with Latitude and longitude values. Then, you can simply import the package and call mergingdata() method which will return you a dataframe with three additionally soil values (Sand value, ECE and Depth of Soil) from feature store which are horizontally row matched which the provided raw data. With the help of this, one can include more attributes that can help train machine learning to gain better results.
