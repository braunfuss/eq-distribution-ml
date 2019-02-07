# eq-distribution-ml
Basic foreshock-aftershock-distribution pattern machine learning with tensorflow

A very basic example on how the tensorflow playground example can be used to learn foreshock-aftershock patterns. 

The idea is that it downloads catalog data and labels all foreshocks with a different label than aftershocks. The time for each can be specified in the get_events.py file.Placeholder times are given for the Amatrice eq.
The position of the shocks are calculated relative to the origin of the mainshock to keep dimensions simple. There is no time parameter right now.

To execute you have to run run.py, where you can also modify how many neurons and hidden layers should be considered under the class Run() (sorry again for the mess but at this stage a config file would make no sense). A lot of the options are hardcoded there. They are the same options as available on the playground demo.

I recommend that you first test it if you like by setting test = True in run.py. 
Then it will just use a gaussian distributed example(you can also generate other example with dataset.py to match the ones in the playground). 
The output will be generated in the folder above in the folder outputs, including images of the model and data distributions as on the playground. 
