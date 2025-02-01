// Models for the MedicalAppt Collection

// Import dependencies.
import mongoose from 'mongoose';
import 'dotenv/config';

// Connect based on the .env file parameters.
mongoose.connect(
    process.env.MONGODB_CONNECT_STRING,
    { useNewUrlParser: true }
);
const db = mongoose.connection;

// Confirm that the database has connected and print a message in the console.
db.once("open", (err) => {
    if(err){
        res.status(500).json({ Error: 'Unable to connect to the database. Please ensure that the MongoDB connection string is correct and the server is running.' });
    } else  {
        console.log('Success: The program successfully connected to the medical appointments and procedures database.');
    }
});

// SCHEMA: Define the collection's schema.
const medicalApptSchema = mongoose.Schema({
	apptType: { type: String, required: true },
	cptCode:  { type: Number, required: true },
	date:     { type: Date,   required: true, default: Date.now }
});

// Compile the model from the schema 
// by defining the collection name "medicalAppts".
const medicalAppts = mongoose.model('MedicalAppts', medicalApptSchema);


// CREATE model *****************************************
const createMedicalAppt = async (apptType, cptCode, date) => {
    const medicalAppt = new medicalAppts({ 
        apptType: apptType, 
        cptCode: cptCode, 
        date: date 
    });
    return medicalAppt.save();
}


// RETRIEVE model *****************************************
// Retrieve all documents and return a promise.
const retrieveMedicalAppts = async () => {
    const query = medicalAppts.find();
    return query.exec();
}

// RETRIEVE by ID
const retrieveMedicalApptByID = async (_id) => {
    const query = medicalAppts.findById({_id: _id});
    return query.exec();
}

// DELETE model based on _id  *****************************************
const deleteMedicalApptById = async (_id) => {
    const result = await medicalAppts.deleteOne({_id: _id});
    return result.deletedCount;
};


// UPDATE model *****************************************************
const updateMedicalAppt = async (_id, apptType, cptCode, date) => {
    const result = await medicalAppts.replaceOne({_id: _id }, {
        apptType: apptType,
        cptCode: cptCode,
        date: date
    });
    return { 
        _id: _id, 
        apptType: apptType,
        cptCode: cptCode,
        date: date 
    }
}

// EXPORT the variables for use in the controller file.
export { createMedicalAppt, retrieveMedicalAppts, retrieveMedicalApptByID, updateMedicalAppt, deleteMedicalApptById }