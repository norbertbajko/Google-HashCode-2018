# Team - Dynamic Duo

![HashCode 2018 Banner](https://cdn-images-1.medium.com/max/1000/1*L-GP2xJWQKFVIgAyTv44ZQ.png)

> Hash Code is a team programming competition organized by Google for students
> and industry professionals across Europe, the Middle East and Africa.
> You pick your team and programming language, we pick a Google engineering 
> problem for you to solve.

## Online Qualification Round
### Self-driving rides
#### Introduction

The problem statement can be found [here](https://hashcode.withgoogle.com/2018/tasks/hashcode2018_qualification_task.pdf).

> Millions of people commute by car every day; for example, to school or to their workplace.
>
> Self-driving vehicles are an exciting development for transportation.
> They aim to make traveling by car safer and more available while also saving commuters time.
>
> In this competition problem, we’ll be looking at how a fleet of self-driving vehicles can efficiently get commuters to their destinations in a simulated city. 

#### Task

> Given a list of pre-booked rides in a city and a fleet of self-driving vehicles,
> assign the rides to vehicles, so that riders get to their destinations on time.
>
> For every ride that finishes on time (or early), you will earn points
> proportional to the distance of that ride;
> plus an additional bonus if the ride also started precisely on time.

#### Usage of our code

Run our scipt with ```python hashcode.py```


There is one notable parameter for tuning the algorithm:
```python
distance_penalty_multiplier = 3
```
which is multiply the penalty for each job per car based on the distance between them.

You can change the input and output files name with:
```python
input_file = './input/d_metropolis.in'
output_file = 'd.txt'
```

#### Results (Extended Round)

| Task               | Score         |
| :----------------- | -------------:|
| A - example        | 10            |
| B - should be easy | 176,877        |
| C - no hurry       | 15,294,233      |
| D - metropolis     | 10,399,799      |
| E - high bonus     | 21,465,945      |
| __Total__          | __47,336,864__      |



## Authors

Norbert Bajko / [@norbertbajko](https://github.com/norbertbajko)  
Peter Nagy    / [@nagypeterjob](https://github.com/nagypeterjob)  

  
The README.md is based on [this one](https://github.com/sbrodehl/Hashcode2k18)

## License

This project is licensed under MIT - see the [LICENSE](LICENSE) file for details
