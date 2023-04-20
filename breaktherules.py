import subprocess

repo_path = '/content/volatile-concentration-localux'

codetorun = """
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui /content/volatile-concentration-localux
!git clone https://huggingface.co/embed/negative /content/volatile-concentration-localux/embeddings/negative
!git clone https://huggingface.co/embed/lora /content/volatile-concentration-localux/models/Lora/positive
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/embed/upscale/resolve/main/4x-UltraSharp.pth -d /content/volatile-concentration-localux/models/ESRGAN -o 4x-UltraSharp.pth
!wget https://raw.githubusercontent.com/camenduru/stable-diffusion-webui-scripts/main/run_n_times.py -O /content/volatile-concentration-localux/scripts/run_n_times.py
!git clone -b v2.1 https://github.com/camenduru/deforum-for-automatic1111-webui /content/volatile-concentration-localux/extensions/deforum-for-automatic1111-webui
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui-images-browser /content/volatile-concentration-localux/extensions/stable-diffusion-webui-images-browser
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui-huggingface /content/volatile-concentration-localux/extensions/stable-diffusion-webui-huggingface
!git clone -b v2.1 https://github.com/camenduru/sd-civitai-browser /content/volatile-concentration-localux/extensions/sd-civitai-browser
!git clone -b v2.1 https://github.com/camenduru/sd-webui-additional-networks /content/volatile-concentration-localux/extensions/sd-webui-additional-networks
!git clone -b v2.1 https://github.com/camenduru/sd-webui-tunnels /content/volatile-concentration-localux/extensions/sd-webui-tunnels
!git clone -b v2.1 https://github.com/camenduru/batchlinks-webui /content/volatile-concentration-localux/extensions/batchlinks-webui
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui-catppuccin /content/volatile-concentration-localux/extensions/stable-diffusion-webui-catppuccin
!git clone -b v2.1 https://github.com/camenduru/a1111-sd-webui-locon /content/volatile-concentration-localux/extensions/a1111-sd-webui-locon
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui-rembg /content/volatile-concentration-localux/extensions/stable-diffusion-webui-rembg
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui-two-shot /content/volatile-concentration-localux/extensions/stable-diffusion-webui-two-shot
!git clone -b v2.1 https://github.com/camenduru/sd_webui_stealth_pnginfo /content/volatile-concentration-localux/extensions/sd_webui_stealth_pnginfo
"""

codetorun2 = """
!git reset --hard
!git -C /content/volatile-concentration-localux/repositories/stable-diffusion-stability-ai reset --hard
"""

lines = codetorun.splitlines()

def rulesbroken(codetoexecute, cwd=''):
    for line in lines:
        line = line.strip()
        if line.startswith('!'):
            line = line[1:]
        if not line == '':
            try:
                if cwd:
                    subprocess.run(line, shell=True, check=True, cwd=repo_path)
                else:
                    subprocess.run(line, shell=True, check=True)
            except Exception as e:
                print("Exception: " + str(e))

rulesbroken(lines)

lines = codetorun2.splitlines()

rulesbroken(lines, repo_path)

