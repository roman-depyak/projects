import products from '../data/products.js';
import OrderRow from './OrderRow.jsx';
import { useState } from 'react';

function OrderPage({ products }){
    const [subtotals, setSubtotals] = useState(products.map(() => 0));

    const updateSubtotal = (index, quantity, price) => {
        const newSubtotals = [subtotals];
        newSubtotals[index] = quantity * price;
        setSubtotals(newSubtotals);
    };

    const runningTotal = subtotals.reduce((acc, curr) => acc + curr, 0);

            return (
                <>
                    <h2>Order</h2>
                    <article>
                        <p></p>
                        <table id="order">
                            <caption>Current Products</caption>
                            <thead>
                                <tr>
                                    <th>Company</th>
                                    <th>Product</th>
                                    <th>Price</th>
                                    <th>Quantity</th>
                                    
                                </tr>
                            </thead>
                            <tbody>
                            {products.map((product, i) => 
                                <OrderRow 
                                    product={product} 
                                    key={i} 
                                    index={i}
                                    subtotal={subtotals[i]}
                                    updateSubtotal={updateSubtotal}
                                />)}
                            </tbody>
                            <tfoot>

                            </tfoot>

                        </table>
                        <h3></h3>
                        <p></p>
                    </article>
                </>
            )
        }
        
export default OrderPage;