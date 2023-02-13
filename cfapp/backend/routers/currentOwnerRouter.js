import express from 'express';
import CurrentOwner from '../models/currentOwner.js';
const router = express.Router();

//Get all current owners
router.get(`/`, async (req, res) => {
    const ownerList = await CurrentOwner.find();
    res.send(ownerList);
})

//Get crop by currentOwnerID
router.get(`/id/:id`, async (req, res) => {
    let currentOwner = await CurrentOwner.find().where('currentOwnerID').equals(req.params.id);
    res.send(currentOwner);
})

//Get current owner by name
router.get(`/name/:name`, async (req, res) => {
    //Allows for lower case queries
    let words = req.params.name.split(" ");
    for (let i = 0; i < words.length; i++) {
        words[i] = words[i][0].toUpperCase() + words[i].slice(1);
    }
    words = words.join(" ");
    let currentOwner = await CurrentOwner.find().where('name').equals(words);
    res.send(currentOwner);
})

//Get current owner by relationship to original owner
router.get(`/relationship/:relationship`, async (req, res) => {
    //Allows for lower case queries
    let lower = req.params.relationship.toLowerCase();
    const ownerList = await CurrentOwner.find();
    const match = ownerList.find(owner => owner.relationshipToOriginalOwners.toLowerCase() === lower);
    
    console.log(match);
    //let lower = req.params.relationship.toLowerCase();
    //let currentOwner = await CurrentOwner.find().where('relationshipToOriginalOwners').equals(lower);
    res.send(match);
})

export default router;