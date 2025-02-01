import OrderQuantity from "./OrderQuantity.jsx";

function OrderRow({ product, index }) {
            return (
                <tr>
                    <td>{product.company}</td>
                    <td>{product.product}</td>
                    <td>{product.price.toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 2 })}<div className="priceColumn"></div></td>
                    <td>
                        <OrderQuantity 
                        index={index}
                        price={product.price}
                        
                        />
                    </td>

                </tr>
            );
        }
        
export default OrderRow;