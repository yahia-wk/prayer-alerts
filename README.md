# Prayer Alerts 📢
This is a program to be run in the background in your home lab stations to play adhan for prayers automatically.

This would work nicely with a Raspberry Pi connected to a central house speaker so adhans are broadcast across a home when it is time for prayer.

## Setting Up ⬇️
To get all the dependencies for the program, install all libraries needed using the environment.yaml file inside a Conda environment

In your Conda environment, run this in your bash terminal:
```
conda env create -f environment.yaml
```
then run:
```
conda activate prayer-alerts
```

## Usage ⏯️
### Customization 🛠️
#### Location 🗺️
You should set the `location` variable appropriately to your desired location
#### Scheduled Time ⏲️
Change at which time of the day you would like the new adhans for the day to be fetched in the `scheduled_time` variable.
NOTE: `scheduled_time` should always be in 24-hour format (e.g. 19:07 and not 7:07 PM) 
#### Adhan Audio 🔉
It is very easy to change the adhan you want to be played for specific prayers. Simply just get your favorite adhan in a `.mp3` file, and rename it to adhan you want that sound to be played for.

The names the program expects for the audio files are: `Fajr.mp3`, `Dhuhr.mp3`, `Asr.mp3`, `Maghrib.mp3`, `Isha.mp3`

### Running The Program ❗
Just run the Python file before the scheduled time you have set in the code:
```
python main.py
```
Then, your machine will play adhan sounds during the correct prayer times.

## Side Note
The program uses [al-adhan API](https://pypi.org/project/aladhan-api/) which depending on your madhab, can get slightly different prayer times for your area.

## Contributing
Feel free to contribute to this project by opening PR to master :)
