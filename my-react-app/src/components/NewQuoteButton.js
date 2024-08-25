import React from 'react';

function NewQuoteButton({ fetchQuote }) {
    return (
        <button onClick={fetchQuote} className="new-quote-button">
            New Quote
        </button>
    );
}

export default NewQuoteButton;
