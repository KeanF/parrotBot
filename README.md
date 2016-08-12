# parrotBot

Simple Twitter feed parrot trained with unweighted Markov Chains (contributed by [@cameronblandford](https://github.com/cameronblandford))

## Usage

### Initial Config

In `./twitter_scraper`
- Supply your own [Twitter API keys](https://apps.twitter.com/)
- Fill in `screen_name` with according to the Twitter API keys

### Examples

Consult `example.py` for some usage examples

## Environment Config

Dependencies
- General: `requirements.txt`
- Windows: [Anaconda](https://www.continuum.io/downloads) for Python 2.7
    + With Anaconda, run
```
conda install conda pip six nose numpy scipy
conda install mingw libpython
```
- Python 2.7
    + [numpy](http://www.numpy.org/), [scipy](https://www.scipy.org/)
    + [tweepy](https://github.com/tweepy/tweepy)
       * With Anaconda, `python -m pip install tweepy`

## Future Considerations

- Refactor for better tweepy cache support
- Static AWS or Heroku instance
- Utilize Keras/Theano for better ML strategies
    + Optional Config (deprecated for Keras/Theano)
        * CUDA (if you have an NVIDIA GPU)
            1. Download and install [Visual Studio Community 2013](https://www.visualstudio.com/us-us/downloads/download-visual-studio-vs.aspx). You do not need any Web or Silverlight dependencies
            2. Download and install [CUDA 7.5](https://developer.nvidia.com/cuda-downloads) with "Express" installation.
            3. Check if CUDA is working by opening *Samples_vs2013.sln* and running any project
                - Right-click *5_Simulations/oceanFFT*
                - *Debug > Start new instance*
                - Build project
                - You should see a simulated ocean surface
            4. Add `C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin` to the `PATH` Environment Variable
            5. When Theano is configured:
                - Add an Environment Variable named `THEANO_FLAGS` with the value `floatX=float32,device=gpu,nvcc.fastmath=True`

