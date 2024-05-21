{ pkgs, ... }: {
  channel = "stable-23.11"; # or "unstable"
  packages = [ pkgs.python3 ];
  idx = {
    extensions = [ "ms-python.python" ];
    workspace = {
      onCreate = {
        install =
          "python -m venv .venv         && source .venv/bin/activate         && pip install -r requirements.txt";
      };
    };
    previews = {
      enable = true;
      previews = {
        web = {
          command = [ "./devserver.sh" ];
          env = { PORT = "$PORT"; };
          manager = "web";
        };
      };
    };
  };
}
