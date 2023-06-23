# SquishCV

A simple Computer Vision Image-Classification that compares an image to a database of Squishmallows 🧸 and finds the "perfect" match.

<p align="center">
  <img height=200 src="https://github.com/KevinWu098/SquishCV/assets/100006999/72d5b4d5-ae47-4761-96ac-d29bb046e650" alt="Person punching a Squishmallow'"
</p>

## Introduction
Computer Vision is rapidly being adopted and improved everyday with applications in countless industries like Self-Driving, Healthcare, Robotics, and even Retail.

Yet, why not have a little fun and see which Squishmallow your pet resembles? Or how about a nice picture of yourself? Who knows, you might be an ["Austin The Avocado!"](https://squishmallowsquad.fandom.com/wiki/Austin)

Built for people who want a quick chuckle (or just a light exhale through the nose), SquishCV is here to add a little bit of joy (and squishiness) to your day.

## Features
Simply upload an image into the simple UI and SquishCV will respond with:
- A cute and cuddly Squishmallow that it deems most similar
- ["It Was Made For Me! This Is My Squishmallow!"](https://knowyourmeme.com/memes/it-was-made-for-me-this-is-my-hole)

<p align="center">
  <img width="800" alt="Dog Squishmallow" src="https://github.com/KevinWu098/SquishCV/assets/100006999/185781d7-df19-40f5-8c13-3a8f1302b95a">
</p>

<p align="center">
  <img width="800" alt="Woman Squishmallow response" src="https://github.com/KevinWu098/SquishCV/assets/100006999/1c28b231-3ae6-4551-b5c1-dcc977d72508">
</p>

## Running SquishCV
Access a live demo of SquishCV hosted on HuggingFace: [SquishCV](https://huggingface.co/spaces/hamlegs/SquishCV)

You can also run a local version with the `gradio` and `DeepImageSearch` packages. This current version uses a [custom fork of DeepImageSearch](https://github.com/KevinWu098/DeepImageSearch) that allows the HuggingFace Spaces to run without EOF errors. But if you're only running it locally, `DeepImageSearch` will serve you well.

## Built With:
- Gradio
- DeepImageSearch
- 420 (🍃) Images scraped from [Squishbase.app](https://squishbase.app/)
