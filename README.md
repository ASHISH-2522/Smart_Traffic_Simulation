# Smart Traffic Simulation System

## Overview
The Smart Traffic Simulation System is a PyGame-based application that simulates intelligent traffic management at a 4-way intersection. This system dynamically adjusts traffic signal timing based on real-time vehicle density, prioritizes emergency vehicles, and provides visual analytics for traffic flow optimization.

## Key Features

- **Adaptive Signal Control**: Dynamically adjusts green light duration based on vehicle volume
- **Emergency Vehicle Priority**: Automatically detects and prioritizes ambulances
- **Multi-Vehicle Simulation**: Supports cars, buses, trucks, bikes, rickshaws, and ambulances
- **Real-time Analytics**: Tracks vehicle counts and traffic metrics
- **Object Tracking**: Implements vehicle tracking algorithms
- **Visual Simulation**: Intuitive PyGame-based visualization

## Installation

### Prerequisites
- Python 3.7+
- PyGame library

### Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/ASHISH-2522/Smart_Traffic_Simulation.git
cd Smart_Traffic_Simulation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the simulation:
```bash
python src/traffic_controller.py
```

## Usage

### Running the Simulation
Execute the main script to start the traffic simulation:
```bash
python src/traffic_controller.py
```

### Controls
- The simulation runs automatically
- Close the window to exit
- Press `ESC` to terminate early

### Configuration
Adjust simulation parameters in `src/traffic_controller.py`:
```python
# Timing parameters
DEFAULT_RED_TIME = 150
DEFAULT_GREEN_TIME = 20
MIN_GREEN_TIME = 10
MAX_GREEN_TIME = 60

# Simulation duration (seconds)
SIMULATION_DURATION = 600
```

## Project Structure

```
Smart_Traffic_Simulation/
├── src/                     # Source code
│   ├── traffic_controller.py # Main simulation logic
│   └── object_tracker.py    # Vehicle tracking implementation
├── assets/                  # Resource files
│   ├── images/              # Visual assets
│   │   ├── vehicles/        # Vehicle images by direction
│      └── signals/         # Traffic signal images
├── docs/                    # Documentation
├── requirements.txt         # Dependencies
├── run_simulation.bat       # Windows execution script
└── run_simulation.sh        # Linux/Mac execution script
```

## Technical Components

### Traffic Controller
- Implements adaptive signal timing algorithm
- Manages vehicle spawning and movement
- Handles emergency vehicle prioritization
- Provides real-time traffic analytics

### Object Tracker
```python
class ObjectTracker:
    def __init__(self):
        self.object_centers = {}
        self.next_id = 0
    
    def update_positions(self, detected_objects):
        # Tracking logic implementation
```

## Results
The simulation provides real-time metrics:
- Vehicles passed per signal
- Total vehicles passed
- Vehicles per unit time
- Emergency vehicle response times

![Simulation Analytics](https://via.placeholder.com/600x300.png?text=Traffic+Analytics+Dashboard)

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, please contact:
- **Ashish Khatode** - [agkhatode25@gmail.com](mailto:agkhatode25@gmail.com)
- Project Repository: [https://github.com/ASHISH-2522/Smart_Traffic_Simulation](https://github.com/ASHISH-2522/Smart_Traffic_Simulation)

