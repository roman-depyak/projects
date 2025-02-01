import { useState } from 'react';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';

import Slogan from './modules/Slogan.jsx';
import GalleryPage from './modules/GalleryPage.jsx';
import HomePage from './modules/HomePage.jsx';
import OrderPage from './modules/OrderPage.jsx';
import TopicsPage from './modules/TopicsPage.jsx';
import MedicalApptsPage from './modules/medicalAppts/MedicalApptsPage.jsx';
import Navigation from './modules/Navigation.jsx';
import products from './data/products.js';
import MedicalApptAdd from './modules/medicalAppts/MedicalApptAdd.jsx'
import MedicalApptEdit from './modules/medicalAppts/MedicalApptEdit.jsx'
import { GiMedicines } from "react-icons/gi";
import './App.css'

function App() {
  const [medicalAppt, setMedicalAppt] = useState([]);

  return (
    <>
      <header>
        <h1>Roman Depyak<i><GiMedicines /></i></h1>
      </header>
      <Slogan />

      <Router>
      <Navigation />
        <main>
            <section>
                <Routes>
                    <Route path="/gallery" element={<GalleryPage />}></Route>
                    <Route path="/" element={<HomePage />}></Route>
                    <Route path="/order"   element={<OrderPage products={products} />}></Route>
                    <Route path="/topics" element={<TopicsPage />}></Route>
                    <Route path="/order"   element={<OrderPage products={products} />}></Route>
                    <Route path="/create" element={<MedicalApptAdd />} />
                    <Route path="/update" element={<MedicalApptEdit medicalApptToEdit={medicalAppt} />}></Route>
                    <Route path="/medicalApptsPage" element={<MedicalApptsPage setMedicalAppt={setMedicalAppt} />}></Route>
                </Routes>
            </section>
        </main>
      </Router>

      <footer>
        <p>&copy; {new Date().getFullYear()} Roman Depyak</p>
      </footer>
    </>
  )
}

export default App
