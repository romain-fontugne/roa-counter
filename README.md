# roa-counter
Plot the number of ROAs over time. 

Data is retrieved from the RIPE RPKI archive: https://ftp.ripe.net/ripe/rpki/


# Installation
```zsh
git clone https://github.com/romain-fontugne/roa-counter.git
cd roa-counter
sudo pip install -r requirements.txt
```

# Usage
```zsh
python count.py
```

The above command creates two figures (pdf and a png) in the current directory
that show the time evolution of the number of ROAs.

![Number of ROAs over time](https://raw.githubusercontent.com/romain-fontugne/roa-counter/main/roa_count_2018_2021.png)
