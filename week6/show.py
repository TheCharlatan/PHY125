# coding: utf-8
from pylab import figure, show, imread, imshow, contourf
from pylab import array, linspace, pi, sin, cos, matrix
from matplotlib.animation import FuncAnimation
from itertools import count
from numpy import radians
from time import time
from time import gmtime


class Map(object):
    """ class showing a map with some contour on it

    Attributes
    ----------
    levels : levels used for the colormap
    main_grid : grid in which the individual sunshine intensities are calculated
    img : Holds the background image
    now: Holds the time on class initialisation
    day: Angle of the earth rotating around its own axis
    year: Angle of the earth rotating around the sun
    N : Resolution of the simulation
    """

    fig = figure()
    img = None
    now = None
    day = None
    year = None
    N = 30
    levels = linspace(-1, 1, 30)
    main_grid = array([[0.0 for x in range(30)] for x in range(30)])
    axes = fig.add_subplot(111)
    inclination = radians(23.5)


    def __init__(self, map_source="karte.png"):
        """ initialise a Map instance

        Parameters
        ----------
        map_source : string
            map-image to use for the background
        """
        self.img = imread(map_source)
        self.img_height = self.img.shape[0]
        self.img_width = self.img.shape[1]
        self.veclatitude = radians(linspace(-90, 90, self.N))
        self.veclongitude = radians(linspace(-180, 180, self.N))
        self.height = linspace(0, self.img_height, self.N)
        self.width = linspace(0, self.img_width, self.N)
        self.axes.xaxis.set_visible(False)
        self.axes.yaxis.set_visible(False)


    def SetTime(self,t):
        """" Set the time after every iteration

        Parameters
        ----------
        t : float
            seconds since Epoch of the time to show
        """
        self.day = ((t.tm_hour+(t.tm_min/60))/24)*2*pi
        self.year = ((t.tm_yday -79)/365)*2*pi

    def Rot_x(self,x):
        """ Returns rotation matrix in x direction

        Parameters
        ----------
        x: float
           Angle to rotate the matrix with
        """
        return matrix([[1,      0,      0],
                       [0, cos(x), sin(x)],
                       [0,-sin(x), cos(x)]])

    def Rot_y(self,y):
        """ Returns rotation matrix in y direction

        Parameters
        ----------
        y: float
           Angle to rotate the matrix with
        """
        return matrix([[cos(y), 0, -sin(y)],
                       [     0, 1,       0],
                       [sin(y), 0,  cos(y)]])

    def Rot_z(self,z):
        """ Returns rotation matrix in z direction

        Parameters
        ----------
        z: float
           Angle to rotate the matrix with
        """
        return matrix([[ cos(z), sin(z), 0],
                       [-sin(z), cos(z), 0],
                       [      0,      0, 1]])

    def Zenith(self, latitude, longitude, day, year, inclination):
        """ Returns a row vector which stands perpendicular to the gound

        Paramters
        ---------
        latitude: float
                  Latitude in Radians
        longitude: flaot
                  Longitude in Radians
        day:      float
                  Angle of the earth relative to the sun depending on its axial rotation
        year:     float
                  Angle of the earth relative to the sun depending on its rotation around the sun
        inclinatio: float
                  Tilt of the earth

        """
        zenith_vector =  matrix([[1,0,0]]) * self.Rot_y(-latitude) * self.Rot_z(longitude+day+year) * self.Rot_x(inclination)
        return zenith_vector[0]

    def Sun(self, year):
        """ Returns a row vector for the position of the sun relative to the surface of the earth
        Parameters
        ----------
        year: float
              Angle of the earth relative ot the sun depending on its rotation around the sun
        """
        return matrix([[1,0,0]]) * self.Rot_z(year)

    def RotateAll(self):
        for long_coor in range(self.N):
          for lat_coor in range(self.N):
            zenith = self.Zenith(self.veclatitude[lat_coor], self.veclongitude[long_coor], self.day, self.year, self.inclination)
            sun = self.Sun(self.year)
            result = sun * zenith.T
            #print(zenith, sun, result)
            self.main_grid[lat_coor][long_coor] = float(result) * (-1)
        return self.main_grid


    def ShowTime(self, t):
        """ show map and contour for a given time t

        Parameters
        ----------
        t : gmtime
            gmtime object gives accurate time in seconds, minutes, hours, days...

        """
        imshow(self.img)
        self.SetTime(t)
        Z = self.RotateAll()
        contourf(self.width, self.height, Z, self.levels, cmap="hot", alpha=0.5)

    def ShowAnimation(self, speed=1800, fps=10):
        """ show animated contour on map

        Parameters
        ----------
        speed : int or float
            seconds passing in the animation for each realtime second
        fps : int
            frames per second of the animation

        """
        start = time()

        def Frame(n):
            """ draw frame n of the animation

            Parameters
            ----------
            n : int
                number of frame to draw (use to calculate time)

            """
            # reset frame before drawing
            self.axes.clear()
            # calculate new time (seconds since Epoche)
            t = gmtime(n*speed)
            # call drawing function
            self.ShowTime(t)

        anim = FuncAnimation(self.fig, Frame, count(), interval=1000/fps)
        show()


if __name__== "__main__":
    demo = Map()
    demo.ShowAnimation()
