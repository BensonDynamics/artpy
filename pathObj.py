import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

class PathObject():
    """Create single path from a line-like image"""
    def __init__(self, imageArray, threshold = 200, scale = 3):
        self.imageArray = imageArray

        #B/W conversion
        self.imageArray[self.imageArray > threshold] = 0
        self.imageArray[self.imageArray > 0] = 1



    def show_original(self):
        """Quick Rendition of the original image. Good for tuning the threshold"""
        plt.imshow(self.imageArray)
        plt.show()


    def tour(self, start = 'random', plot = True):
        """Get A*A tour through pixels"""
        #Credit to @alexpmil for this section. Notice the similar var names.
        abs_index = np.where(self.imageArray > 0)  # positions of non-zero pixels
        rel_index = np.array(range(1, len(abs_index) + 1))

        # Replace each non-zero pixel in the array with its number
        # i.e., the 10th non-zero pixel will have 10 in its place
        flat_img_mod = deepcopy(self.imageArray)

        for rel, pix in abs_index:
            flat_img_mod[pix] = rel + 1

        """

        # Get coordinates for each non-zero pixel
        img_idx = np.reshape(flat_img_mod, self.imageArray.shape)
        self.coord_list = []
        for p1 in rel_index:
            p1_coords = tuple([int(c) for c in np.where(img_idx == p1)])
            self.coord_list.append(list(p1_coords))

        # Calculate distance between each pair of coords
        dist_mat = distance.cdist(self.coord_list, self.coord_list, 'euclidean')

        # Initialize search space with nearest neighbor tour
        cities = self.coord_list
        num_cities = len(cities)
        if starting_point == "random":
            start = int(np.random.choice(range(num_cities), size=1))
        else:
            assert starting_point < num_cities
            start = starting_point
        tour = [start]
        active_city = start
        for step in range(0, num_cities):
            dist_row = deepcopy(dist_mat[active_city, :])
            for done in tour:
                dist_row[done] = np.inf
            nearest_neighbor = np.argmin(dist_row)
            if nearest_neighbor not in tour:
                tour.append(nearest_neighbor)
            active_city = nearest_neighbor

        y_tour = -np.array([cities[tour[i % num_cities]] for i in range(num_cities + 1)])[:, 0]
        y_tour = y_tour - y_tour[0]  # - min(y_tour)
        x_tour = np.array([cities[tour[i % num_cities]] for i in range(num_cities + 1)])[:, 1]
        x_tour = x_tour - x_tour[0]  # - min(x_tour)

        # Circle tour back to beginning
        np.append(x_tour, x_tour[0])
        np.append(y_tour, y_tour[0])
        num_cities = num_cities + 1

        self.x_tour = x_tour
        self.y_tour = y_tour
        self.num_pixels = num_cities

        if plot:
            plt.plot(self.x_tour, self.y_tour)
            plt.show()

        """
        return abs_index, rel_index, flat_img_mod


    def path(self):
        return


