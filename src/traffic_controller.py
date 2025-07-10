import random
import math
import time
import threading
import pygame
import sys
import os

# Configuration constants
DEFAULT_RED_TIME = 150
DEFAULT_YELLOW_TIME = 5
DEFAULT_GREEN_TIME = 20
MIN_GREEN_TIME = 10
MAX_GREEN_TIME = 60

traffic_lights = []
TOTAL_LIGHTS = 4
SIMULATION_DURATION = 150
elapsed_time = 0

active_green_index = 0
next_green_index = (active_green_index + 1) % TOTAL_LIGHTS
yellow_active = 0

# Vehicle traversal times
VEHICLE_TIMES = {
    'car': 2,
    'bike': 1,
    'rickshaw': 2.25,
    'bus': 2.5,
    'truck': 2.5,
    'ambulance': 2.5
}

# Vehicle counts
vehicle_counts = {
    'car': 0,
    'bike': 0,
    'bus': 0,
    'truck': 0,
    'rickshaw': 0,
    'ambulance': 0
}
LANE_COUNT = 2

# Detection parameters
DETECTION_THRESHOLD = 5
VEHICLE_SPEEDS = {'car': 2.25, 'bus': 1.8, 'truck': 1.8, 
                 'rickshaw': 2, 'bike': 2.5, 'ambulance': 1.8}

# Coordinate mappings
start_coords = {
    'right': {'x': [0, 0, 0], 'y': [348, 370, 398]},
    'down': {'x': [755, 727, 697], 'y': [0, 0, 0]},
    'left': {'x': [1400, 1400, 1400], 'y': [498, 466, 436]},
    'up': {'x': [602, 627, 657], 'y': [800, 800, 800]}
}

traffic_objects = {
    'right': {0: [], 1: [], 2: [], 'crossed': 0},
    'down': {0: [], 1: [], 2: [], 'crossed': 0},
    'left': {0: [], 1: [], 2: [], 'crossed': 0},
    'up': {0: [], 1: [], 2: [], 'crossed': 0}
}

VEHICLE_TYPES = {0: 'car', 1: 'bus', 2: 'truck', 
                3: 'rickshaw', 4: 'bike', 5:'ambulance'}
DIRECTION_MAP = {0: 'right', 1: 'down', 2: 'left', 3: 'up'}

# UI coordinates
signal_coords = [(530, 230), (810, 230), (810, 570), (530, 570)]
timer_coords = [(530, 210), (810, 210), (810, 550), (530, 550)]
counter_coords = [(480, 210), (880, 210), (880, 550), (480, 550)]
counter_texts = ["0", "0", "0", "0"]

# Traffic stop positions
stop_lines = {'right': 590, 'down': 330, 'left': 800, 'up': 535}
default_stops = {'right': 580, 'down': 320, 'left': 810, 'up': 545}
dynamic_stops = {'right': [580, 580, 580], 'down': [320, 320, 320], 
                'left': [810, 810, 810], 'up': [545, 545, 545]}

midpoints = {
    'right': {'x': 705, 'y': 445},
    'down': {'x': 695, 'y': 450},
    'left': {'x': 695, 'y': 425},
    'up': {'x': 695, 'y': 400}
}
ROTATION_ANGLE = 3

# Vehicle spacing
STOP_GAP = 15
MOVE_GAP = 15

pygame.init()
simulation_group = pygame.sprite.Group()

class TrafficLight:
    def __init__(self, red_time, yellow_time, green_time, min_time, max_time):
        self.red_time = red_time
        self.yellow_time = yellow_time
        self.green_time = green_time
        self.min_time = min_time
        self.max_time = max_time
        self.display_text = "30"
        self.total_green_duration = 0

class TrafficVehicle(pygame.sprite.Sprite):
    def __init__(self, lane, vehicle_type, direction_id, direction, will_turn):
        pygame.sprite.Sprite.__init__(self)
        self.lane = lane
        self.vehicle_type = vehicle_type
        self.speed = VEHICLE_SPEEDS[vehicle_type]
        self.direction_id = direction_id
        self.direction = direction
        self.x = start_coords[direction]['x'][lane]
        self.y = start_coords[direction]['y'][lane]
        self.crossed = 0
        self.will_turn = will_turn
        self.turned = 0
        self.rotation = 0
        
        traffic_objects[direction][lane].append(self)
        self.index = len(traffic_objects[direction][lane]) - 1
        
        # Path updated for new structure
        img_path = f"assets/images/vehicles/{direction}/{vehicle_type}.png"
        self.original_img = pygame.image.load(img_path)
        self.current_img = pygame.image.load(img_path)
        
        # Position initialization logic
        self.initialize_position()

    def initialize_position(self):
        # Position calculation logic remains same
        # [Original position initialization code]
        
        simulation_group.add(self)
    
    def render(self, screen):
        screen.blit(self.current_img, (self.x, self.y))
    
    def move(self):
        # Movement logic remains same
        # [Original movement code]

def setup_traffic_lights():
    # Initialization logic
    # [Original initialization code]

def calculate_green_time():
    global vehicle_counts
    # Green time calculation logic
    # [Original setTime function]

def run_signal_cycle():
    global active_green_index, yellow_active, next_green_index
    # Signal cycling logic
    # [Original repeat function]

def display_signal_status():
    # Status display logic
    # [Original printStatus function]

def update_timers():
    # Timer update logic
    # [Original updateValues function]

def spawn_vehicles():
    # Vehicle generation logic
    # [Original generateVehicles function]

def spawn_ambulances():
    # Ambulance generation logic
    # [Original generateVehiclesAmb function]

def track_simulation_time():
    global elapsed_time
    # Time tracking logic
    # [Original simulationTime function]

class SimulationApp:
    # Main application class
    # [Restructured Main class]