import { useState } from 'react'
import { FaArrowCircleUp } from "react-icons/fa";
import { FaArrowCircleDown } from "react-icons/fa";

function ProductQuantity() {
            const [quantity, setQuantity] = useState(0);

            const incrementQuantity = () => {
                        if (quantity < 10) {
                                    const newQuantity = quantity + 1;
                                    setQuantity(newQuantity);
                                    updateSubtotal(index, newQuantity * price);
                                }
            };

            const decrementQuantity = () => {
                        if (quantity > 0) {
                                    const newQuantity = quantity - 1;
                                    setQuantity(newQuantity);
                                    updateSubtotal(index, newQuantity * price);
                                }
            }

            return (
                        <div className="clicker">
                                    <i><FaArrowCircleUp onClick={incrementQuantity} /></i>
                                    {quantity}
                                    <i><FaArrowCircleDown onClick={decrementQuantity} /></i>
                        </div>
            );
}

export default ProductQuantity;