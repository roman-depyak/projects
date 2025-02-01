// Controllers for the MedicalAppt Collection

import 'dotenv/config';
import express from 'express';
import * as medicalAppts from './medical-appt-model.mjs';

const PORT = process.env.PORT;
const app = express();
app.use(express.json());  // REST needs JSON MIME type.


// CREATE controller ******************************************
app.post ('/medicalAppts', (req,res) => { 
    medicalAppts.createMedicalAppt(
        req.body.apptType, 
        req.body.cptCode, 
        req.body.date
        )
        .then(medicalAppt => {
            console.log(`"${medicalAppt.apptType}" was added to the collection of medical appointments and procedures.`);
            res.status(201).json(medicalAppt);
        })
        .catch(error => {
            console.log(error);
            res.status(400).json({ Error: 'There was a client error processing the request, likely due to invalid JSON structure. Please ensure the appointment type is a word, the CPT code is a number, and the date is in the format MM-DD-YYYY.' });
        });
});


// RETRIEVE controller ****************************************************
app.get('/medicalAppts', (req, res) => {
    medicalAppts.retrieveMedicalAppts()
        .then(medicalAppts => { 
            if (medicalAppts !== null) {
                console.log(`All medical appoointments and procedures were retrieved successfully from the collection.`);
                res.json(medicalAppts);
            } else {
                res.status(404).json({ Error: 'The requested medical appointment or procedure was not found in the collection.' });
            }         
         })
        .catch(error => {
            console.log(error);
            res.status(400).json({ Error: 'A client error occurred. Ensure that all required fields have been entered with a valid appointment type, CPT code, and date.' });
        });
});


// RETRIEVE by ID controller
app.get('/medicalAppts/:_id', (req, res) => {
    medicalAppts.retrieveMedicalApptByID(req.params._id)
    .then(medicalAppt => { 
        if (medicalAppt !== null) {
            console.log(`"${medicalAppt.apptType}" was retrieved, based on its ID.`);
            res.json(medicalAppt);
        } else {
            res.status(404).json({ Error: 'Unable to locate the medical appointment or procedure in the collection. The provided ID may not exist in the database. Ensure that the appointment type, CPT Code, and date have been entered correctly.' });
        }         
     })
    .catch(error => {
        console.log(error);
        res.status(400).json({ Error: 'Invalid request. The provided ID is not in a valid format.' });
    });

});


// UPDATE controller ************************************
app.put('/medicalAppts/:_id', (req, res) => {
    medicalAppts.updateMedicalAppt(
        req.params._id, 
        req.body.apptType, 
        req.body.cptCode, 
        req.body.date
    )
    .then(medicalAppt => {
        console.log(`"${medicalAppt.apptType}" was updated.`);
        res.json(medicalAppt);
    })
    .catch(error => {
        console.log(error);
        res.status(400).json({ Error: 'Failed to update medical appointment or procedure. Please ensure that appointment type, CPT Code, and date have been entered and are valid.' });
    });
});


// DELETE Controller ******************************
app.delete('/medicalAppts/:_id', (req, res) => {
    medicalAppts.deleteMedicalApptById(req.params._id)
        .then(deletedCount => {
            if (deletedCount === 1) {
                console.log(`Based on its ID, ${deletedCount} medical appointment was deleted.`);
                res.status(200).send({ Success: 'The medical appointment or procedure was successfully deleted.' });
            } else {
                res.status(404).json({ Error: 'No medical appointment or procedure was found with the provided ID. The appointment was not deleted.' });
            }
        })
        .catch(error => {
            console.error(error);
            res.send({ Error: 'The provided ID is invalid. Ensure that the ID is in the correct format and has been entered correctly.' });
        });
});


app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`);
});