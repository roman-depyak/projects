import React from 'react';
import MedicalAppt from './MedicalAppt.jsx';

function MedicalApptList({ medicalAppts, onDelete, onEdit}) {
            return (
                        <table id="medicalAppts">
                                    <caption>Add and Edit Medical Appointments</caption>
                                    <thead>
                                                <tr>
                                                            <th>Appointment Type</th>
                                                            <th>CPT Code</th>
                                                            <th>Date</th>
                                                            <th>Delete</th>
                                                            <th>Edit</th>
                                                </tr>
                                    </thead>
                                    <tbody>
                                                {medicalAppts.map((medicalAppt, i) =>
                                                            <MedicalAppt
                                                                        medicalAppt={medicalAppt}
                                                                        key={i}
                                                                        onDelete={onDelete}
                                                                        onEdit={onEdit}
                                                />)}
                                    </tbody>
                        </table>
            )
}

export default MedicalApptList;