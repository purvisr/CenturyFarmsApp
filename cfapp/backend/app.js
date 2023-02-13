import * as dotenv from 'dotenv'; 
dotenv.config();

import express from 'express';
import bodyParser from 'body-parser';
import mongoose from 'mongoose';
import cropRouter from './routers/cropRouter.js';
import livestockRouter from './routers/livestockRouter.js';
import farmDescriptionRouter from './routers/farmDescriptionRouter.js';
import currentOwnerRouter from './routers/currentOwnerRouter.js';
import morgan from 'morgan';
import cors from 'cors';

const app = express();

app.use(cors());
app.options('*', cors());

const api = process.env.API_URL;
const connection_string = process.env.CONNECTION_STRING;


app.use(bodyParser.json());
app.use(morgan('tiny'));
app.use(`${api}/crop`, cropRouter);
app.use(`${api}/farmdesc`, farmDescriptionRouter);
app.use(`${api}/livestock`, livestockRouter);
app.use(`${api}/currentOwner`, currentOwnerRouter);

mongoose.connect(connection_string, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    //strictQuery: true,
    dbName: 'CFDB'
})
.then(() =>{
    console.log('Database is connected')
})
.catch((err)=> {
    console.log(err);
})


app.listen(3000, ()=>{
    console.log(api);
    console.log('Server is running on port 3000');
})