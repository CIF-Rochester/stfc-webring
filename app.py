import random
from urllib.parse import urlparse
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

def parse_sites(filename="sites.txt"):
    sites = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.count("--") < 2:
                    continue
                parts = [p.strip() for p in line.split("--", 2)]
                url, domain_controlled, name = parts[0], parts[1], parts[2]
                sites.append({
                    "url": url,
                    "domain_controlled": domain_controlled.lower(),
                    "name": name
                })
    except FileNotFoundError:
        pass
    return sites

def find_current_index(sites):
    current_url = request.args.get('current', '').strip()
    if not current_url and request.referrer:
        current_url = request.referrer.strip()
    print(f"--- DEBUG: current_url = {current_url} ---")
    if not current_url:
        return -1
    if "://" not in current_url:
        current_url = "http://" + current_url
    parsed_current = urlparse(current_url)
    current_netloc = parsed_current.netloc.lower()
    current_path = parsed_current.path.lower().rstrip('/')
    for i, site in enumerate(sites):
        controlled = site['domain_controlled']
        if '/' in controlled:
            target_full = f"//{controlled}".lower().rstrip('/')
            current_full = f"//{current_netloc}{current_path}".lower().rstrip('/')
            if current_full.startswith(target_full):
                return i
        else:
            if current_netloc == controlled:
                return i
    for i, site in enumerate(sites):
        if site['url'].rstrip('/') == current_url.rstrip('/') :
            return i
    return -1

# Default Route-- Display all members of the webring in one neat, convenient little package.  
@app.route("/")
def list_sites():
    sites = parse_sites()
    return render_template("members.html", sites=sites)

# Random Member Redirect
@app.route("/random")
def random_redirect():
    lines = []
    try:
        with open("sites.txt", "r") as f:
            lines = [line.strip() for line in f if line.strip() and line.count("--") >= 2]
    except FileNotFoundError:
        pass
    if not lines:
        return redirect(url_for('list_sites'))
    selected_line = random.choice(lines)
    target_url = selected_line.split("--", 2)[0].strip()
    return redirect(target_url, code=302)

# Next Member Route
@app.route("/next")
def next_site():
    sites = parse_sites()
    if not sites:
        return redirect(url_for('list_sites'))
    currentIndex = find_current_index(sites)
    if currentIndex == -1 or currentIndex >= len(sites) - 1:
        next_url = sites[0]['url']
    else:
        next_url = sites[currentIndex + 1]['url']
    return redirect(next_url, code=302)

# Previous Member Route
@app.route("/previous")
def prev_site():
    sites = parse_sites()
    if not sites:
        return redirect(url_for('list_sites'))
    currentIndex = find_current_index(sites)
    if currentIndex <= 0:
        prev_url = sites[-1]['url']
    else:
        prev_url = sites[currentIndex - 1]['url']
    return redirect(prev_url, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
