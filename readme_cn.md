
## 参考 https://docs.khoj.dev/advanced/litellm/

```shell

conda activate zen
which pip
# Install Khoj for Development
pip install -e '.[proxy]'
```

开始
```bash
#export MISTRAL_API_KEY=<MISTRAL_API_KEY>
conda activate zen
litellm --model mistral/mistral-tiny --drop_params

```