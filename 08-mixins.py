class Gun:
    def fire(self):
        pass

    def reload(self):
        pass


class FrozenGunThemeMixin:
    ...


class SniperMixins:
    def zoom(self):
        pass


class AWP(Gun, SniperMixins, FrozenGunThemeMixin):
    ...
