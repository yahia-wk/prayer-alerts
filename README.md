# Prayer Alerts 📢
This is a program to be run in the background in your home lab stations to automatically play adhan times for prayers.

This would work nicely with a Rasbperry Pi connected to a central house speaker so adhans are broadcasted across a home.

## Setting Up ⬇️
To get all the dependancies for the program, install all libraries needed using the environment.yaml file inside a Conda environment

In your Conda environment, run this in your bash terminal:
```
conda env create -f environment.yaml
```
then run:
```
conda activate prayer-alerts
```

## Usuage ⏯️
### Customization 🛠️
#### Location 🗺️
You should the `location` variable appropriately to your desired location
#### Scheduled Time ⏲️
Change at which time of the day you would like the new adhans for the day to be fetched in the `scheduled_time` variable.

NOTE: `scheduled_time` should always be in 24 hour format (e.g. 19:07 and not 7:07 PM) 

### Running The Program ❗
Just run the python file before the scheduled time you have set in the code:
```
python main.py
```
and then your machine will play adhan sounds at the correct prayer times.

## Contributing
Feel free to contribute to this project by opening PR to master :)
