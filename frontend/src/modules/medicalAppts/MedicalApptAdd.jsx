import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export const MedicalApptAdd = () => {
    const [apptType,    setApptType]    = useState('');
    const [cptCode,     setCptCode]     = useState('');
    const [date,        setDate]        = useState(''); 

    const redirect = useNavigate();

    const addMedicalAppt = async (event) => {
        event.preventDefault();

        const newMedicalAppt = { apptType, cptCode, date };
        try {
            const response = await fetch('/medicalAppts', {
                method: 'POST',
                body: JSON.stringify(newMedicalAppt),
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            if(response.status === 201){
                alert(`The medical appointment or procedure was successfully added to the collection.`);
                redirect("/medicalApptsPage");
            } else {
                alert(`A problem occurred while adding the medical appointment and it was not added. Please try again later. Status code: = ${response.status}`);
            }
        } catch (error) {
            alert(`A problem occurred while connecting to the server. Please check your internet connection and try again. Error: = ${response.status}`);
        }
    }

    return (
        <>
            <h2>Add a medical appointment</h2>
            <article>
            <p>You can add a medical appointment or procedure by clicking on the 'Add a medical appointment' button. When adding the appointment or procedure please include the appointment type, CPT code, and date.</p>

            <table id="medicalAppts">
                <caption>Which medical appointment are you adding?</caption>
                <thead>
                    <tr>
                        <th>Appointment Type</th>
                        <th>CPT Code</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                <tr>
                    <td><label htmlFor="apptType">Appointment Type</label>
                    <input
                        type="text"
                        placeholder="Visit Type"
                        value={apptType}
                        onChange={e => setApptType(e.target.value)}
                        id="apptType" />
                    </td>

                    <td><label htmlFor="cptCode">CPT Code</label>
                    <input
                        type="number" min="1" max="99499"
                        placeholder="CPT Code"
                        value={cptCode}
                        onChange={e => setCptCode(e.target.value)}
                        id="cptCode" />
                    </td>

                    <td><label htmlFor="date">Date</label>
                    <input
                        type="date"
                        placeholder="Date of the medical appointment or procedure"
                        value={date}
                        onChange={e => setDate(e.target.value)}
                        id="date" />
                    </td>

                    <td>
                    <label htmlFor="submit">Commit</label>
                        <button
                            type="submit"
                            onClick={addMedicalAppt}
                            id="submit"
                        >Add</button>
                    </td>
                </tr>
                </tbody>
            </table>
            </article>
        </>
    );
}

export default MedicalApptAdd;