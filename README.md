# Teachable Machine model on Raspberry Pi 4 
Software for running TeachableMachine Keras model on Raspberry Pi 4 developed for [nvias.org](https://nvias.org/) by [Marek Ruttner](https://www.linkedin.com/in/marek-ruttner-826b90177/), [David Žahour](https://www.linkedin.com/in/david-%C5%BEahour-64072b166/)

## Requirements
- RPI 4 with camera
- [installed Tensorflow 2](https://qengineering.eu/install-tensorflow-2.1.0-on-raspberry-pi-4.html)

## Usage 
1. Fork this repository
2. Train your model on [TeachableMachine](https://teachablemachine.withgoogle.com)
3. Download your trained model as TensorFlow Keras model
4. Unzip and paste *converted_keras* into your directory with forked repo
5. Commit changes
6. Pull changes on your RPI and run `pyhton3 main.py`

## License
```
Copyright 2023 nvias.org

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
