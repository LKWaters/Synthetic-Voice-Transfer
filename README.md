# A Deep Convolutional Network Transfer Based on the LJ Speech Dataset and Kyubyoung's Text to Speech Model

The goal of this was to take a speech data set with thousands of samples such as the LJ speech dataset and then once trained significantly on that model begin training with a dataset that consisted of significantly less samples.

[LJ Speech Dataset](https://www.dropbox.com/s/1oyipstjxh2n5wo/LJ_logdir.tar?dl=0).

[Kyubyong's Text to Speech](https://github.com/Kyubyong/dc_tts).

## Process

Becasue this is based on Kyubyongs model if youre looking for in depth information about how to get a text to speech model like this working you should check out his link as I will only be covering how I transfered the model over to the voice of my choice and then implemented it on a discord server for ease of acess.

One thing you notice imediately is that without the huge premade dataset it takes a LONG time to create and transcribe your own. the LJ dataset has over 13,000 samples of pre transcribed audio and its a breeze to work with. Now when it comes to making the voice of your choice you either have to be lucky enough to find a premade dataset or creat your own. 

Because I wanted to create a speech model based off of Teo, a popular streamer and youtuber, I had to transcribe and sample my own audio.[Teo's Twitch](https://www.twitch.tv/teosgame),[Teo's Youtube](https://www.youtube.com/channel/UCDa8HbNrmkFhKKOeiB7JaRw).

![](fig/Teoirl.jpg)

