import React from 'react';
import { FaRegEdit } from "react-icons/fa";
import { FaRegTrashCan } from "react-icons/fa6";

function MedicalAppt({ medicalAppt, onEdit, onDelete }) {
            return (
                        <tr>
                                    <td>{medicalAppt.apptType}</td>
                                    <td>{medicalAppt.cptCode}</td>
                                    <td>{medicalAppt.date.slice(0,10)}</td>
                                    <td><i><FaRegTrashCan onClick={() => onDelete(medicalAppt._id)} /></i></td>
                                    <td><i><FaRegEdit onClick={() => onEdit(medicalAppt)} /></i></td>
                        </tr>
            )
}

export default MedicalAppt;
