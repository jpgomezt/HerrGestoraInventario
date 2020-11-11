<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Color extends Model
{
    public $timestamps = false;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'color_name', 'color_hex',
    ];
}
