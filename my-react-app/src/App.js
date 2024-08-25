import React, { useState, useEffect } from 'react';
import QuoteDisplay from './components/QuoteDisplay';
import NewQuoteButton from './components/NewQuoteButton';
import SaveQuote from './components/SaveQuote';
import SavedQuotesList from './components/SavedQuotesList';
import Footer from './components/Footer';

function App() {
    const [quote, setQuote] = useState({});
    const [savedQuotes, setSavedQuotes] = useState([]);

    const fetchQuote = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/quotes/');
            const data = await response.json();
            setQuote(data);
        } catch (error) {
            console.error('Error fetching the quote:', error);
        }
    };

    const fetchSavedQuotes = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/saved-quotes/');
            const data = await response.json();
            setSavedQuotes(data);
        } catch (error) {
            console.error('Error fetching saved quotes:', error);
        }
    };

    const saveQuote = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/save-quote/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    quote: quote.quote,
                    author: quote.author,
                }),
            });

            const data = await response.json();
            console.log(data);

            // Update the saved quotes list in real-time
            setSavedQuotes([...savedQuotes, { quote: quote.quote, author: quote.author }]);

        } catch (error) {
            console.error('Error saving the quote:', error);
        }
    };

    useEffect(() => {
        fetchQuote();
        fetchSavedQuotes(); 
    }, []);

    return (
        <div className="App">
            <div className="quote-container">
                <QuoteDisplay quote={quote} />
                <NewQuoteButton fetchQuote={fetchQuote} />
                <SaveQuote saveQuote={saveQuote} />
            </div>
            <SavedQuotesList savedQuotes={savedQuotes} /> {}
            <Footer />
        </div>
    );
}

export default App;
