<h1>About</h1>
This is the backend for the REST API. API creation with django and django-rest-framework. Parser for Beautiful Soup 4.
<h2>Deploy</h2>
<ol>
  <li>Clone this repo</li>
  <li>Install requirements
    <ul>
      <li>Create virtual env (<code>python -m venv .venv</code>)</li>
      <li>Activate virtual env (On Linux/OSX: <code>source .venv/bin/activate</code>, On Windows: <code>.venv/Scripts/Activate.bat</code>)</li>
      <li>Install requirements (<code>pip install -r requirements.txt</code>)</li>
    </ul>
  </li>
  <li>Next, you need to configure the django server itself via wsgi or asgi. It is located in the "ExchangeRates" directory</li>
</ol>
<h2>Docs</h2>
<ul>
  <li>Only Get requests are available</li>
  <li>Get "/" will redirect you to "/usd/"</li>
  <li>Get /currency/ will answer you with a list with the currency rates you specified (Available currency rates: usd, eur, gbp, chf)</li>
  <li>If you add the name of the bank to the previous one, the answer will contain data only for the bank you specified</li>
</ul>
