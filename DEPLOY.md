# Deploy di Io sono / Ariane

## Obiettivo attuale

Pubblicare subito la home page come sito statico, mantenendo gia pronta la struttura per collegare in seguito il backend della chat di Ariane.

## Stato del progetto

- `frontend/index.html` e pronto per un deploy statico
- la chat usa una configurazione runtime opzionale tramite `window.ARIANE_CONFIG`
- se nessuna configurazione e presente, la pagina prova a usare `http://localhost:5000`
- quando il backend non e collegato, la home resta comunque funzionante e mostra un messaggio chiaro

## Deploy statico consigliato

La soluzione piu semplice e pubblicare la cartella `frontend` su Netlify.

### Netlify

1. collega il repository Git
2. imposta come cartella di pubblicazione `frontend`
3. in alternativa, usa il file `netlify.toml` gia incluso nella root di `ariane-ai`

## Collegare Ariane in seguito

Quando il backend Flask verra pubblicato, potrai impostare prima di `index.html` una configurazione come questa:

```html
<script>
window.ARIANE_CONFIG = {
  apiBaseUrl: "https://tuo-backend-online.example.com"
};
</script>
```

In questo modo la stessa home continuera a funzionare senza modificare il codice della pagina.

## Roadmap consigliata

1. pubblicare la home statica
2. creare una pagina dedicata ad Ariane
3. pubblicare il backend Flask su un servizio come Render o Railway
4. collegare la home e la futura pagina Ariane all'URL pubblico del backend
