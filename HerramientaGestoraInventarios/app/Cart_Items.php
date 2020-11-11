<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Cart_Items extends Model
{
    public $timestamps = false;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'user_id', 'cart_id',
    ];
}
