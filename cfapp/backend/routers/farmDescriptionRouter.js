import express from 'express';
import FarmDescription from '../models/farmDescription.js';
const router = express.Router();

//Get all farm descriptions
router.get(`/`, async (req, res) => {
    const farmList = await FarmDescription.find();
    res.send(farmList);
})

//Get farm description by farmPastID
router.get(`/farmPastID/:id`, async (req, res) => {
    let farm = await FarmDescription.find().where('farmPastID').equals(req.params.id);
    res.send(farm);
})

//Get farm description by farmCurrentID
router.get(`/farmCurrentID/:id`, async (req, res) => {
    let farm = await FarmDescription.find().where('farmCurrentID').equals(req.params.id);
    res.send(farm);
})

//Get farm description by currentOwnerID
router.get(`/currentOwnerID/:id`, async (req, res) => {
    let farm = await FarmDescription.find().where('currentOwnerID').equals(req.params.id);
    res.send(farm);
})

//Get farm description by originalOwnerID
router.get(`/originalOwnerID/:id`, async (req, res) => {
    let farm = await FarmDescription.find().where('originalOwnerID').equals(req.params.id);
    res.send(farm);
})

//Get farm description by locationID
router.get(`/locationID/:id`, async (req, res) => {
    let farm = await FarmDescription.find().where('locationID').equals(req.params.id);
    res.send(farm);
})

//Get farm description by name
router.get(`/name/:name`, async (req, res) => {
    //Allows for lower case queries
    let words = req.params.name.split(" ");
    for (let i = 0; i < words.length; i++) {
        words[i] = words[i][0].toUpperCase() + words[i].slice(1);
    }
    words = words.join(" ");

    let farm = await FarmDescription.find().where('name').equals(words);
    res.send(farm);
})

//Get farm description by award year
router.get(`/year/:year`, async (req, res) =>{
    let yearInt = parseInt(req.params.year);
    let farms = await FarmDescription.find().where('yearOfAward').equals(yearInt);
    console.log(farms);
    console.log(req.params.year);
    console.log(typeof yearInt);
    res.send(farms);
})

//Get farm description by award type
router.get(`/award/:name`, async (req, res) => {
    //Allows for lower case queries
    let words = req.params.name.split(" ");
    for (let i = 0; i < words.length; i++) {
        words[i] = words[i][0].toUpperCase() + words[i].slice(1);
    }
    words = words.join(" ");

    let farm = await FarmDescription.find().where('awardType').equals(words);
    res.send(farm);
})

export default router;