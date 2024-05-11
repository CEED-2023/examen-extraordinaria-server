Prepare environment:
```sh
pip install virtualenv
python -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run:
```sh
python -m flask run --reload
```

Call endpoints:

- **GET /chats**: get a list of all chats.

Input: none

Response:
```json
[
	{
		"id": 1,
		"title": "Chat 1"
	}
]
```
- **POST /chat**: creates a chat.

Input:
```json
{
	"messages": [
		{ "role": "user", "message": "This is a message" },
		{ "role": "assistant", "message": "This is an assistant message" }
	]
}
```
Response:
```json
{
	"id": 1,
	"title": "Chat 1"
}
```
- **GET /chat/:id**: get chat's data

Response:
```json
[
	{
		"role": "user",
		"message": "This is a message"
	},
	{
		"role": "assistant",
		"message": "This is an assistant message"
	}
]
```

- **POST /chat/completions**: get response from the IA

Input (last message must be with role "user"):
```json
{
	"messages": [
		{
			"role": "user",
			"content": "Hola, como estás"
		},
		{
			"role": "assistant",
			"content": "Muy bien, dime en que te puedo ayudar hoy"
		},
		{
			"role": "user",
			"content": "Dime un pareado"
		}
	]
}
```

Response:
```json
{
	"message": "¡Claro! Aquí te dejo uno:\n\n\"El que espera desespera,\ny el que busca encuentra.\"\n\n¿Te gustó?"
}

```

### Deploy

fly secrets set GROQ_API_KEY=<your api key>
fly deploy



