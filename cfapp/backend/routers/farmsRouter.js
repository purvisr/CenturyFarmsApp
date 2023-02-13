import express from 'express';
import Farm from '../models/farms.js';
const router = express.Router();

router.get(`/`, async (req, res) => {
    const farmList = await Farm.find();
    res.send(farmList);
})

router.get(`/year/:year`, async (req, res) =>{
    let yearInt = parseInt(req.params.year);
    let farms = await Farm.find().where('Year_Of_Award').equals(yearInt);
    console.log(farms);
    console.log(req.params.year);
    console.log(typeof yearInt);
    res.send(farms);
})

router.post(`/`, (req, res) =>{
    const farm = new Farm({
        name: req.body.name,
        currentOwner: req.body.currentOwner,
        awardType: req.body.awardType,
        yearOfAward: req.body.yearOfAward
    })
    farm.save().then((createdFarm=> {
        res.status(201).json(createdFarm)
    })).catch((err)=>{
        res.status(500).json({
            error:err
        })
    })
})


export default router;