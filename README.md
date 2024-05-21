# Multilayer Perceptron

An implementation of a Multilayer Perceptron using NumPy and Pandas, with a Tkinter GUI.

## Setup

1. Install Python >= 3.11.4
2. Install required packages

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the following command to start the application

```bash
python main.py
```

### Notes

- The datasets are stored in the `data/` directory. Each dataset has a handler in `src/data_handlers.py` that is responsible for cleaning, preprocessing, and train-test splitting.

- The multilayer perceptron is implemented in `src/model.py`.
- Logs of the training process are stored in the `logs/` directory.
