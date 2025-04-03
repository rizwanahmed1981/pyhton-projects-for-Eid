
# Enter a weight on earth: 120
# The equivalent weight on Mars: 45.36




# we use constants!
MARS_MULTIPLE = 0.378

def main():
    # Technically weight is measured in newtons, but one of your
    # goals is to focus on the python, not the physics!
    earth_weight_str = input('Enter a weight on earth: ')

    # input() returns a value in string form, get the number out
    earth_weight = float(earth_weight_str)

    # More variables is good times when first learning
    mars_weight = earth_weight * MARS_MULTIPLE

    # Note the string concatenation!
    print('The equivalent weight on Mars: ' + str(mars_weight))

if __name__ == '__main__':
    main()