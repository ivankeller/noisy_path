# helpers.py

import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        return np.sqrt((self.end_point.x - self.start_point.x)**2 + (self.end_point.y - self.start_point.y)**2)

class Path:
    def __init__(self, segments):
        self.segments = segments

    def length(self):
        return sum([segment.length() for segment in self.segments])

    def plot(self, ax=None, color='r', marker='o', alpha=1):
        if ax is None:
            fig, ax = plt.subplots()
        
        x_coords = []
        y_coords = []
        
        for segment in self.segments:
            x_coords.append(segment.start_point.x)
            y_coords.append(segment.start_point.y)
        
        # Add the last point of the last segment
        x_coords.append(self.segments[-1].end_point.x)
        y_coords.append(self.segments[-1].end_point.y)
        
        ax.plot(x_coords, y_coords, color=color, marker=marker, alpha=alpha)
        
        return ax



def generate_random_path(n_segments):
    segments = []
    for i in range(n_segments):
        start_point = Point(np.random.rand(), np.random.rand())
        end_point = Point(np.random.rand(), np.random.rand())
        segments.append(Segment(start_point, end_point))
    return Path(segments)

def generate_straight_path(n_segments, length):
    segments = []
    for i in range(n_segments):
        start_point = Point(i * length, 0)
        end_point = Point((i + 1) * length, 0)
        segments.append(Segment(start_point, end_point))
    return Path(segments)

def add_gaussian_noise(path, sigma):
    noisy_segments = []
    for segment in path.segments:
        noisy_start_point = Point(segment.start_point.x + np.random.normal(0, sigma), segment.start_point.y + np.random.normal(0, sigma))
        noisy_end_point = Point(segment.end_point.x + np.random.normal(0, sigma), segment.end_point.y + np.random.normal(0, sigma))
        noisy_segments.append(Segment(noisy_start_point, noisy_end_point))
    return Path(noisy_segments)