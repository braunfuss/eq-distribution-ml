from pyrocko import util, model
from pyrocko.client import catalog
import numpy as num
from random import shuffle

latmin = 41.
latmax = 44.
lonmin = 12.7
lonmax = 13.9

# more categories could be inlcuded easily.
tmin_mainshock = util.str_to_time('2016-08-24 01:30:00')  # amatrice event
tmax_mainshock = util.str_to_time('2016-08-24 01:39:59')

tmin_foreshocks = util.str_to_time('2009-04-06 01:00:00')  # 
tmax_foreshocks = util.str_to_time('2016-08-24 01:30:59')

tmin_aftershocks = util.str_to_time('2016-01-01 01:40:00')  #aftershocks
tmax_aftershocks = util.str_to_time('2019-01-30 23:59:59')

def create_event_file():
    global_usgs_catalog = catalog.USGS()


    mainshock = global_usgs_catalog.get_events(
        time_range=(tmin_mainshock, tmax_mainshock),
        magmin=6.,
        latmin=latmin,
        latmax=latmax,
        lonmin=lonmin,
        lonmax=lonmax)
    mainshock = mainshock[0]
    foreshocks = global_usgs_catalog.get_events(
        time_range=(tmin_foreshocks, tmax_foreshocks),
        magmin=0.,
        latmin=latmin,
        latmax=latmax,
        lonmin=lonmin,
        lonmax=lonmax)

    aftershocks = global_usgs_catalog.get_events(
        time_range=(tmin_aftershocks, tmax_aftershocks),
        magmin=0.,
        latmin=latmin,
        latmax=latmax,
        lonmin=lonmin,
        lonmax=lonmax)

    lats = []
    lons = []
    pids = []
    labels = []
    for i,event in enumerate(foreshocks):
        lats.append(mainshock.lat-event.lat)
        lons.append(mainshock.lon-event.lon)
        pids.append(i)
        labels.append(1)
    for j,event in enumerate(aftershocks):
        lats.append(mainshock.lat-event.lat)
        lons.append(mainshock.lon-event.lon)
        pids.append(i+j)
        labels.append(-1)

    num.random.seed(0)
    shuffle(lats)
    num.random.seed(0)
    shuffle(lons)
    num.random.seed(0)
    shuffle(labels)
    filename = 'data.txt'
    with open(filename, 'w') as f:
        column_names = ['pid']
        column_names.append('X1')
        column_names.append('X2')
        column_names.append('label')
        header_str = '\t'.join(column_names)
        f.write(header_str + '\n')
        for i in range(len(pids)):
            label = labels[i]
            row_str = [str(i)]
            row_str.append(str(lats[i]))
            row_str.append(str(lons[i]))
            row_str.append(str(label))
            row_str = '\t'.join(row_str)
            f.write(row_str + '\n')
