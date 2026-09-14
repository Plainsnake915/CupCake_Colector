import pygame
import asyncio  # 1. Import asyncio

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Place your game loop inside an async function
async def main():  # 2. Add 'async' before your main function definition
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # --- Your Game Logic & Drawing Code Here ---
        screen.fill((0, 0, 0)) 
        pygame.display.flip()
        
        await asyncio.sleep(0)  # 3. CRITICAL: Add this at the VERY END of your while loop

# Run the game using asyncio
asyncio.run(main())  # 4. Initialize the loop


### Step 2.5: Rules for Custom .png Images
#Web browsers handle assets much more strictly than your local computer. If your game uses custom images, you must follow these rules or your web player will crash with a File Not Found error:

#* Use Lowercase Names Only: Ensure all folders and .png file names use strictly lowercase letters (e.g., use assets/cupcake.png, not Assets/Cupcake.PNG). Web servers are strictly case-sensitive. Relative Paths Only: Load your images using relative paths starting from where your main.py sits. 
#  * Correct: pygame.image.load("assets/cupcake.png")
#  * Incorrect: pygame.image.load("C:/Users/Name/Documents/Lab2/assets/cupcake.png")


### Step 3: Create the Automation Workflow & Upload Code
#Instead of building web files on your local computer, GitHub can handle it automatically every time you save.

#1. In your GitHub repository, click Add file > Create new file.
#2. In the "Name your file..." box, type exactly: .github/workflows/deploy.yml (Typing the slashes will create the necessary subfolders automatically).
#3. Paste the following automated script into the file editor:

#```yaml
#name: Deploy Pygame to GitHub Pages

#on:
#  push:
#    branches:
#      - main  
#  workflow_dispatch:

#permissions:
#  contents: write # Grants the workflow permission to publish files to your repository

#jobs:
#  build-and-deploy:
#    runs-on: ubuntu-latest
#    steps:
#      - name: Checkout Code
#        uses: actions/checkout@v4
#
#      - name: Set up Python
#        uses: actions/setup-python@v5
#        with:
#          python-version: '3.11'
#
#      - name: Install Pygbag
#        run: |
#          python -m pip install --upgrade pip
#          pip install pygbag
##      - name: Build Web Files
#        run: |
#          python -m pygbag --build .
#
#      - name: Deploy to GitHub Pages
#        uses: JamesIves/github-pages-deploy-action@v4
#        with:
#          branch: gh-pages
#          folder: build/web
#```
#4. Scroll down, click Commit changes..., and confirm the commit.
#5. Upload Your Game Files & Folders: Click Add file > Upload files. Drag and drop your main.py alongside your entire asset folder (e.g., your assets folder containing the .png files) directly into your root repository layout. Commit the changes.
#
#---
#
#### Step 4: Create a README File
#1. In your repository, click Add file > Create new file.
#2. Name the file README.md.
#3. Write a brief description of your game, the controls, and clear instructions explaining how to play the game. Commit the changes.

#---

#### Step 5: Launch Your Game Link
#1. Click the Actions tab at the top of your repository page to track your build. Wait until you see a green checkmark next to the "Deploy Pygame to GitHub Pages" run.
#2. Go back to your repository's Settings tab.
#3. Click on Pages on the left-hand sidebar.
#4. Under the Build and deployment section:
#   * Set Source to Deploy from a branch.
#   * Under Branch, change None to gh-pages (This branch was automatically built by your workflow script).
#   * Leave the directory folder as / (root) and click Save.
#5. Wait roughly one minute and refresh the page. Your live game link will appear at the top of the panel!

#---
#
### Final Submission Check
#When turning in your assignment, make sure you submit both required URLs:
#* Repository URL: https://github.com/your-username/Lab-2-Cupcake-Collector
#* Live Web Game URL: https://your-username.github.io/Lab-2-Cupcake-Collector/