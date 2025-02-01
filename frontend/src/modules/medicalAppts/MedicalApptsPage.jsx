import { React, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import MedicalApptList from './MedicalApptList';
import { Link } from 'react-router-dom';
import { IoIosAddCircleOutline } from "react-icons/io";

function MedicalApptsPage({ setMedicalAppt }) {
    const redirect = useNavigate();

    const [medicalAppts, setMedicalAppts] = useState([]);

    const loadMedicalAppts = async () => {
        const response = await fetch('/medicalAppts');
        const medicalAppts = await response.json();
        setMedicalAppts(medicalAppts);
    }

    const onEditMedicalAppt = async medicalAppt => {
        setMedicalAppt(medicalAppt);
        redirect("/update");
    }

    const onDeleteMedicalAppt = async _id => {
        const response = await fetch(`/medicalAppts/${_id}`, { method: 'DELETE' });
        if (response.status === 200) {
            const getResponse = await fetch('medicalAppts')
            const medicalAppts = await getResponse.json();
            setMedicalAppts(medicalAppts);
        } else {
            console.error(`There was an error while trying to delete the medical appointment with ID = ${_id}. The appointment was not deleted. Status code = ${response.status}`) 
        }
    }

    useEffect(() => {
        loadMedicalAppts();
    }, []);

            return (
                <>
                    <h2>List of Medical Appointments</h2>
                    <article>
                        <p>Below is a list of medical appointments and procedures. The type of visit, CPT code, and date are provided below.</p>
                        <Link to="/create"><i><IoIosAddCircleOutline /></i></Link>
                        <MedicalApptList
                            medicalAppts={medicalAppts}
                            onEdit={onEditMedicalAppt}
                            onDelete={onDeleteMedicalAppt}
                        />
                    </article>
                </>
            );
        }

export default MedicalApptsPage;