import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export const MedicalApptEdit = ({ medicalApptToEdit }) => {
    const [apptType,    setApptType]    = useState(medicalApptToEdit.apptType);
    const [cptCode,     setCptCode]     = useState(medicalApptToEdit.cptCode);
    const [date,        setDate]        = useState(medicalApptToEdit.date); 

    const redirect = useNavigate();

    const editMedicalAppt = async () => {

        const response = await fetch(`/medicalAppts/${medicalApptToEdit._id}`, {
            method: 'PUT',
            body: JSON.stringify({
                apptType: apptType,
                cptCode: cptCode,
                date: date
            }),
            headers: {'Content-Type': 'application/json',},
        });

        if (response.status === 200) {
            alert('The changes made to your medical appointment have been updated successfully.');
        } else {
            const errMessage = await response.json();
            alert(`There was a problem while updating your appointment details and the changes were not updated successfully. Status: ${response.status}. ${errMessage.Error}`);
        }
        redirect("/medicalApptsPage");
    }

    return (
        <>
        <article>
            <h2>Edit a medical appointment</h2>
            <p>You can edit a medical appointment or procedure by clicking on the 'Edit a medical appointment' button. When editing the appointment or procedure you are able to modify the appointment type, CPT code, and date.</p>
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
                            placeholder="Type of appointment or procedure"
                            value={apptType}
                            onChange={e => setApptType(e.target.value)}
                            id="apptType" />
                        </td>

                        <td><label htmlFor="cptCode">CPT Code</label>
                        <input
                            type="number" min="1" max="99499"
                            placeholder="CPT Code for the appointment or procedure"
                            value={cptCode}
                            onChange={e => setCptCode(e.target.value)}
                            id="cptCode" />
                        </td>

                        <td><label htmlFor="date">Date</label>
                        <input
                            type="date"
                            placeholder="Date of the appointment or procedure"
                            value={date}
                            onChange={e => setDate(e.target.value)}
                            id="date" />
                        </td>

                        <td>
                        <label htmlFor="submit">Commit</label>
                            <button
                                type="submit"
                                onClick={editMedicalAppt}
                                id="submit"
                                >Edit</button>
                        </td>
                    </tr>
                    </tbody>
            </table>
        </article>
        </>
    );
}

export default MedicalApptEdit;