from pygal import *


def main():
    with open('bacteria.csv', 'r') as f:
        data = f.readlines()

    #data is holding a list of strings

    bacteria_count = {}

    for line in data:
        clean_data = line.strip().split(',')
        print(clean_data)
        bacteria = clean_data[0]

        if bacteria in bacteria_count:
            bacteria_count[bacteria] += 1
        else:
            bacteria_count[bacteria] = 1

    bacteria_chart = Bar(width=1600, height=1000, title='Bacterias in a bar graph')

    for bacteria, count in bacteria_count.items():
        bacteria_chart.add(bacteria, count)

    bacteria_chart.render_to_file('bacteria.svg')


main()
