import {useState} from "react";

export const HomePage = () => {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [description, setDescription] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        const response = await fetch('http://127.0.0.1:5000/documents/template', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                first_name: firstName,
                last_name: lastName,
                email: email,
                description: description,
                callback_url: 'http://localhost/'
            }),
        })
        const data = await response.json();
        console.log(data)
        window.open(data.redirect_url, '_blank');

    };
    return (<div className="flex  flex-col gap-3">
            <input type="text" placeholder="First Name" value={firstName} onChange={(e) => setFirstName(e.target.value)}/>
            <input type="text" placeholder="Last Name" value={lastName} onChange={(e) => setLastName(e.target.value)}/>
            <input type="text" placeholder="Email Name" value={email} onChange={(e) => setEmail(e.target.value)}/>
            <textarea placeholder="description" value={description} onChange={(e) => setDescription(e.target.value)}/>

            <button onClick={handleLogin}>Send</button>
        </div>
    )
};
