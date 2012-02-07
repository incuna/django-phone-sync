# Incuna Contacts

Provide a way to push a list of contacts to phone handsets via their base station.


## Backends

The method through which different base stations update their handsets differs so `contacts` provides a backend system to enable access to the different base stations.

Each backend is registered in the `BACKENDS` setting using a path to the class. These classes inherit from the `BaseStation` class which provides a relationship with the Handset class allowing you to define handsets on a base station.

A Django action allows you to push a selection of contacts to all handsets.

