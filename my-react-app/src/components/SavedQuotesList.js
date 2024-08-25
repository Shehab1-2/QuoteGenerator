import React from 'react';

function SavedQuotesList({ savedQuotes }) {  
    return (
        <div className="saved-quotes-list">
            <h3>Saved Quotes</h3>
            <ul>
                {savedQuotes.map((quote, index) => (
                    <li key={index}>
                        "{quote.quote}" - {quote.author}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default SavedQuotesList;
